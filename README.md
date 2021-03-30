# RDC Discord bot

As a fun little side project, I decided to develop a custom Discord bot for the RedDotCity channel. The bot itself will be coded in Python@3 and will have a database service running aswell to keep logs and to save scores etc.

Later I'd love to add music bot support and a lot of fun little features.

## How to run

```sh
python3 -m pipenv shell
pip install -r requirements.txt

pipenv run dev
```

## Dependencies

- Pydantic: Creating and enforcing models
- Discord.py: Core Discord bot hooks
- databases: Async database connector
- SQLAlchemy core: SQL query builder
- colorlog: Log all exceptions and important stuff to text

## Contributors

- Rexani (AmantS)
