-- Run this script in pgAdmin while connected to database "rfid-lokero"

-- Remove legacy tables created earlier in this project.
-- =========================
-- TABLE: oikeustaso
-- =========================
CREATE TABLE IF NOT EXISTS public.oikeustaso (
    oikeustaso INTEGER PRIMARY KEY,
    rooli VARCHAR(20) NOT NULL UNIQUE
);

-- =========================
-- TABLE: lainaaja
-- =========================
CREATE TABLE IF NOT EXISTS public.lainaaja (
    etunimi VARCHAR(50) NOT NULL,
    sukunimi VARCHAR(50) NOT NULL,
    oikeustaso INTEGER NOT NULL,
    tunnus VARCHAR(200) NOT NULL UNIQUE,
    rfid VARCHAR(50) PRIMARY KEY,
    aktiivinen BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (oikeustaso)
        REFERENCES public.oikeustaso(oikeustaso)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- =========================
-- TABLE: lokerikko
-- =========================
CREATE TABLE IF NOT EXISTS public.lokerikko (
    lokero INTEGER PRIMARY KEY,
    mac_osoite VARCHAR(20) NOT NULL UNIQUE
);

-- =========================
-- TABLE: tuote
-- =========================
CREATE TABLE IF NOT EXISTS public.tuote (
    tuotenumero INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    tuote VARCHAR(100) NOT NULL,
    tuotekuvaus VARCHAR(500),
    aktiivinen BOOLEAN NOT NULL DEFAULT TRUE
);

-- =========================
-- TABLE: tuotesijainti
-- =========================
CREATE TABLE IF NOT EXISTS public.tuotesijainti (
    lokero INTEGER NOT NULL,
    tuotenumero INTEGER NOT NULL,
    PRIMARY KEY (lokero, tuotenumero),
    FOREIGN KEY (tuotenumero)
        REFERENCES public.tuote(tuotenumero)
        ON DELETE RESTRICT,
    FOREIGN KEY (lokero)
        REFERENCES public.lokerikko(lokero)
        ON DELETE RESTRICT
);

-- =========================
-- TABLE: lainaus
-- =========================
CREATE TABLE IF NOT EXISTS public.lainaus (
    lainausnumero INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    rfid VARCHAR(50) NOT NULL,
    tuotenumero INTEGER NOT NULL,
    lokero INTEGER NOT NULL,
    lainausaika TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    palautusaika TIMESTAMP,
    FOREIGN KEY (rfid)
        REFERENCES public.lainaaja(rfid)
        ON DELETE RESTRICT,
    FOREIGN KEY (tuotenumero)
        REFERENCES public.tuote(tuotenumero)
        ON DELETE RESTRICT,
    FOREIGN KEY (lokero)
        REFERENCES public.lokerikko(lokero)
        ON DELETE RESTRICT,
    CONSTRAINT chk_aika CHECK (
        palautusaika IS NULL OR palautusaika > lainausaika
    )
);

-- =========================
-- INDEXES
-- =========================
CREATE INDEX IF NOT EXISTS idx_lainaus_rfid ON public.lainaus(rfid);
CREATE INDEX IF NOT EXISTS idx_lainaus_tuotenumero ON public.lainaus(tuotenumero);
CREATE INDEX IF NOT EXISTS idx_lainaus_lokero ON public.lainaus(lokero);

-- =========================
-- PARTIAL INDEX
-- =========================
CREATE UNIQUE INDEX IF NOT EXISTS unique_active_lainaus
ON public.lainaus(tuotenumero)
WHERE palautusaika IS NULL;
