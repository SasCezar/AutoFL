CREATE TABLE project
(
    id          SERIAL  NOT NULL,
    name        VARCHAR NOT NULL,
    version_sha VARCHAR NOT NULL,
    version_num INT     NOT NULL,
    config      JSONB   NOT NULL,
    project     JSONB   NOT NULL,
    version     JSONB   NOT NULL,
    PRIMARY KEY (name, version_sha, config)
);

CREATE TABLE keywords
(
    id          SERIAL  NOT NULL,
    name        VARCHAR NOT NULL,
    version_sha VARCHAR NOT NULL,
    version_num INT     NOT NULL,
    config      JSONB   NOT NULL,
    project     JSONB   NOT NULL,
    version     JSONB   NOT NULL,
    labels      JSONB   NOT NULL,
    PRIMARY KEY (name, version_sha, config)
);