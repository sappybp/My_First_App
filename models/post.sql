CREATE TABLE post (
  id INTEGER PRIMARY KEY,
  postMessage VARCHAR(255),
  postAge VARCHAR(255),
  postGender VARCHAR(255),
  postLike INTEGER default 0,
  postWriterID INTEGER
);
