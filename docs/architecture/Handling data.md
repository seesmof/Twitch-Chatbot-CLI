### Designing database architecture for the app

The app will most likely use database, namely SQLite, in the following places:

- For logging responses
- For storing user credentials

For logging responses the table will have the following structure:

```sql
CREATE TABLE responses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  channel TEXT,
  username TEXT,
  prompt TEXT,
  response TEXT,
);
```

For storing user credentials, namely an authentication, a username and the channels on which the bot will operate, we will need to create the following table:

```sql
CREATE TABLE users (
  authKey TEXT PRIMARY KEY,
  username TEXT,
  channels TEXT,
);
```

Although for the credentials I'm thinking the only JSON file might be sufficient enough, since there shall always be only one user (bot account) logged in at the same time. But we will see about that when we get closer to the implementation phase.

One more note for the responses database - I think it would be nice if the user could have a menu option which would allow them to see all the responses, or entrances in the table, for a specified date.
