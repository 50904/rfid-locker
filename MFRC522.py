#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
#
#    This file is part of MFRC522-Python
#
import platform
import logging

if platform.system() != "Windows":
    import spidev  # type: ignore[import-not-found]
    from gpiozero import DigitalOutputDevice  # type: ignore[import-not-found]
else:
    spidev = None
    DigitalOutputDevice = None


class MFRC522:
    MAX_LEN = 16

    PCD_IDLE = 0x00
    PCD_AUTHENT = 0x0E
    PCD_RECEIVE = 0x08
    PCD_TRANSMIT = 0x04
    PCD_TRANSCEIVE = 0x0C
    PCD_RESETPHASE = 0x0F
    PCD_CALCCRC = 0x03

    PICC_REQIDL = 0x26
    PICC_REQALL = 0x52
    PICC_ANTICOLL = 0x93
    PICC_SElECTTAG = 0x93
    PICC_AUTHENT1A = 0x60
    PICC_AUTHENT1B = 0x61
    PICC_READ = 0x30
    PICC_WRITE = 0xA0
    PICC_DECREMENT = 0xC0
    PICC_INCREMENT = 0xC1
    PICC_RESTORE = 0xC2
    PICC_TRANSFER = 0xB0
    PICC_HALT = 0x50

    MI_OK = 0
    MI_NOTAGERR = 1
    MI_ERR = 2

    CommandReg = 0x01
    CommIEnReg = 0x02
    DivIrqReg = 0x05
    ErrorReg = 0x06
    Status2Reg = 0x08
    FIFODataReg = 0x09
    FIFOLevelReg = 0x0A
    ControlReg = 0x0C
    BitFramingReg = 0x0D

    ModeReg = 0x11
    TxControlReg = 0x14
    TxAutoReg = 0x15
    TModeReg = 0x2A
    TPrescalerReg = 0x2B
    TReloadRegH = 0x2C
    TReloadRegL = 0x2D

    CRCResultRegM = 0x21
    CRCResultRegL = 0x22

    serNum = []

    def __init__(self, bus=0, device=0, spd=1000000, pin_rst=-1, cs_manual=False, cs_pin=8, debugLevel="WARNING"):
        if spidev is None or DigitalOutputDevice is None:
            raise RuntimeError("MFRC522 is not supported on Windows.")

        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        self.spi.max_speed_hz = spd

        self.logger = logging.getLogger("mfrc522Logger")
        if not self.logger.handlers:
            self.logger.addHandler(logging.StreamHandler())
        level = logging.getLevelName(debugLevel)
        self.logger.setLevel(level)

        if pin_rst == -1:
            pin_rst = 15

        if cs_manual is True:
            self._CS = DigitalOutputDevice(cs_pin, initial_value=True)
        else:
            self._CS = None

        self._RST = DigitalOutputDevice(pin_rst, initial_value=True)
        self.MFRC522_Init()

    def MFRC522_Reset(self):
        self.Write_MFRC522(self.CommandReg, self.PCD_RESETPHASE)

    def Write_MFRC522(self, addr, val):
        if self._CS is not None:
            self._CS.toggle()
        self.spi.xfer2([(addr << 1) & 0x7E, val])
        if self._CS is not None:
            self._CS.toggle()

    def Read_MFRC522(self, addr):
        if self._CS is not None:
            self._CS.toggle()
        val = self.spi.xfer2([((addr << 1) & 0x7E) | 0x80, 0])
        if self._CS is not None:
            self._CS.toggle()
        return val[1]

    def Close_MFRC522(self):
        self.spi.close()

    def SetBitMask(self, reg, mask):
        tmp = self.Read_MFRC522(reg)
        self.Write_MFRC522(reg, tmp | mask)

    def ClearBitMask(self, reg, mask):
        tmp = self.Read_MFRC522(reg)
        self.Write_MFRC522(reg, tmp & (~mask))

    def AntennaOn(self):
        temp = self.Read_MFRC522(self.TxControlReg)
        if ~(temp & 0x03):
            self.SetBitMask(self.TxControlReg, 0x03)

    def AntennaOff(self):
        self.ClearBitMask(self.TxControlReg, 0x03)

    def MFRC522_ToCard(self, command, sendData):
        backData = []
        backLen = 0
        status = self.MI_ERR
        irqEn = 0x00
        waitIRq = 0x00

        if command == self.PCD_AUTHENT:
            irqEn = 0x12
            waitIRq = 0x10
        if command == self.PCD_TRANSCEIVE:
            irqEn = 0x77
            waitIRq = 0x30

        self.Write_MFRC522(self.CommIEnReg, irqEn | 0x80)
        self.ClearBitMask(0x04, 0x80)
        self.SetBitMask(self.FIFOLevelReg, 0x80)
        self.Write_MFRC522(self.CommandReg, self.PCD_IDLE)

        for i in range(len(sendData)):
            self.Write_MFRC522(self.FIFODataReg, sendData[i])

        self.Write_MFRC522(self.CommandReg, command)

        if command == self.PCD_TRANSCEIVE:
            self.SetBitMask(self.BitFramingReg, 0x80)

        i = 2000
        while True:
            n = self.Read_MFRC522(0x04)
            i -= 1
            if ~((i != 0) and ~(n & 0x01) and ~(n & waitIRq)):
                break

        self.ClearBitMask(self.BitFramingReg, 0x80)

        if i != 0:
            if (self.Read_MFRC522(self.ErrorReg) & 0x1B) == 0x00:
                status = self.MI_OK
                if n & irqEn & 0x01:
                    status = self.MI_NOTAGERR

                if command == self.PCD_TRANSCEIVE:
                    n = self.Read_MFRC522(self.FIFOLevelReg)
                    lastBits = self.Read_MFRC522(self.ControlReg) & 0x07
                    if lastBits != 0:
                        backLen = (n - 1) * 8 + lastBits
                    else:
                        backLen = n * 8

                    if n == 0:
                        n = 1
                    if n > self.MAX_LEN:
                        n = self.MAX_LEN

                    for _ in range(n):
                        backData.append(self.Read_MFRC522(self.FIFODataReg))
            else:
                status = self.MI_ERR

        return (status, backData, backLen)

    def MFRC522_Request(self, reqMode):
        self.Write_MFRC522(self.BitFramingReg, 0x07)
        status, _, backBits = self.MFRC522_ToCard(self.PCD_TRANSCEIVE, [reqMode])
        if ((status != self.MI_OK) | (backBits != 0x10)):
            status = self.MI_ERR
        return (status, backBits)

    def MFRC522_Anticoll(self):
        self.Write_MFRC522(self.BitFramingReg, 0x00)
        status, backData, _ = self.MFRC522_ToCard(self.PCD_TRANSCEIVE, [self.PICC_ANTICOLL, 0x20])

        if status == self.MI_OK:
            if len(backData) == 5:
                serNumCheck = 0
                for i in range(4):
                    serNumCheck = serNumCheck ^ backData[i]
                if serNumCheck != backData[4]:
                    status = self.MI_ERR
            else:
                status = self.MI_ERR

        return (status, backData)

    def CalulateCRC(self, pIndata):
        self.ClearBitMask(self.DivIrqReg, 0x04)
        self.SetBitMask(self.FIFOLevelReg, 0x80)

        for i in range(len(pIndata)):
            self.Write_MFRC522(self.FIFODataReg, pIndata[i])

        self.Write_MFRC522(self.CommandReg, self.PCD_CALCCRC)
        i = 0xFF
        while True:
            n = self.Read_MFRC522(self.DivIrqReg)
            i -= 1
            if not ((i != 0) and not (n & 0x04)):
                break

        return [self.Read_MFRC522(self.CRCResultRegL), self.Read_MFRC522(self.CRCResultRegM)]

    def MFRC522_SelectTag(self, serNum):
        buf = [self.PICC_SElECTTAG, 0x70]
        for i in range(5):
            buf.append(serNum[i])

        pOut = self.CalulateCRC(buf)
        buf.append(pOut[0])
        buf.append(pOut[1])
        status, backData, backLen = self.MFRC522_ToCard(self.PCD_TRANSCEIVE, buf)

        if (status == self.MI_OK) and (backLen == 0x18):
            return backData[0]
        return 0

    def MFRC522_Auth(self, authMode, BlockAddr, Sectorkey, serNum):
        buff = [authMode, BlockAddr]
        for i in range(len(Sectorkey)):
            buff.append(Sectorkey[i])
        for i in range(4):
            buff.append(serNum[i])

        status, _, _ = self.MFRC522_ToCard(self.PCD_AUTHENT, buff)
        return status

    def MFRC522_StopCrypto1(self):
        self.ClearBitMask(self.Status2Reg, 0x08)

    def MFRC522_Read(self, blockAddr):
        recvData = [self.PICC_READ, blockAddr]
        pOut = self.CalulateCRC(recvData)
        recvData.append(pOut[0])
        recvData.append(pOut[1])
        status, backData, _ = self.MFRC522_ToCard(self.PCD_TRANSCEIVE, recvData)
        if status != self.MI_OK:
            self.logger.error("Error while reading!")

        if len(backData) == 16:
            return backData
        return None

    def MFRC522_Write(self, blockAddr, writeData):
        buff = [self.PICC_WRITE, blockAddr]
        crc = self.CalulateCRC(buff)
        buff.append(crc[0])
        buff.append(crc[1])
        status, backData, backLen = self.MFRC522_ToCard(self.PCD_TRANSCEIVE, buff)
        if (status != self.MI_OK) or (backLen != 4) or ((backData[0] & 0x0F) != 0x0A):
            status = self.MI_ERR

        if status == self.MI_OK:
            buf = []
            for i in range(16):
                buf.append(writeData[i])

            crc = self.CalulateCRC(buf)
            buf.append(crc[0])
            buf.append(crc[1])
            status, backData, backLen = self.MFRC522_ToCard(self.PCD_TRANSCEIVE, buf)
            if (status != self.MI_OK) or (backLen != 4) or ((backData[0] & 0x0F) != 0x0A):
                self.logger.error("Error while writing")

    def MFRC522_Init(self):
        self.MFRC522_Reset()
        self.Write_MFRC522(self.TModeReg, 0x8D)
        self.Write_MFRC522(self.TPrescalerReg, 0x3E)
        self.Write_MFRC522(self.TReloadRegL, 30)
        self.Write_MFRC522(self.TReloadRegH, 0)
        self.Write_MFRC522(self.TxAutoReg, 0x40)
        self.Write_MFRC522(self.ModeReg, 0x3D)
        self.AntennaOn()
