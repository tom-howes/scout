-- Personal Schema for SQL DBs I will implement in SQLAlchemy --
-- Code not to be executed -- 

-- Artists Table --
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    spotify_id VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    genres TEXT[],
    popularity INTEGER,
    followers INTEGER,
    monthly_listeners INTEGER,
    image_url TEXT,
    spotify_url TEXT,
    quality_score FLOAT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Audio Features --
CREATE TABLE audio_features (
    id SERIAL PRIMARY KEY,
    artist_id INTEGER REFERENCES artists(id),
    avg_acousticness FLOAT,
    avg_danceability FLOAT,
    avg_energy FLOAT,
    avg_valence FLOAT,
    avg_tempo FLOAT,
    updated_at TIMESTAMP DEFAULT NOW()
);

-- User Discoveries --
CREATE TABLE discoveries (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255),  -- Simple string for now
    artist_id INTEGER REFERENCES artists(id),
    discovered_at TIMESTAMP DEFAULT NOW(),
    followers_at_discovery INTEGER
);