from models import Hero, Team
from database import engine
from sqlmodel import Session, select, and_, col
from typing import Optional, List


def create_heroes():
    with Session(engine) as session:
        team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret's Bar")
        session.add(team_preventers)
        session.add(team_z_force)
        session.commit()

        session.refresh(team_preventers)
        session.refresh(team_z_force)

        hero_deadpond = Hero(name="Deadpond", secret_name="Dive Wilson", team_id=team_z_force.id)
        hero_rusty_man = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48, team_id=team_preventers.id)
        hero_spider_boy = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        session.commit()

        session.refresh(hero_deadpond)
        session.refresh(hero_rusty_man)
        session.refresh(hero_spider_boy)

        print("Created hero:", hero_deadpond)
        print("Created hero:", hero_rusty_man)
        print("Created hero:", hero_spider_boy)


def get_hero(name: Optional[str] = None):
    with Session(engine) as session:
        if name:
            statement = select(Hero).where(Hero.name == name)  # Fetch a hero by name
            results = session.exec(statement).first()
            response_msg = f"Hero found: {results}" if results else f"No hero found with name: {name}"
            print(response_msg)
        else:
            statement = select(Hero)  # Fetch all heroes
            heroes = session.exec(statement).all()
            if heroes:
                # print(f'All heroes: {heroes}')
                print("All heroes:")
                for hero in heroes:
                    print(hero)
            else:
                print("No heroes found.")


def get_hero_name_and_age(name: Optional[str] = None):
    with Session(engine) as session:
        if name:
            statement = select(Hero.secret_name, Hero.age).where(and_(Hero.name == name, Hero.age > 18))
            result = session.exec(statement).first()
            response = f"Hero found: Secret name: {result[0]}, Age: {result[1]}" if result else f"No hero found with name: {name}"
            print(response)
        else:
            statement = select(Hero.name, Hero.age)  # Select only the secret_name and age of all heroes
            results = session.exec(statement).all()
            if results:
                print("All heroes' names and ages:")
                for result in results:
                    print(f"Name: {result[0]}, Age: {result[1]}")
            else:
                print("No heroes found.")


def delete_hero():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Deadpond")  # Select all heroes from the table
        heroes = session.exec(statement).all()
        for hero in heroes:  # Delete each hero individually
            session.delete(hero)
        session.commit()  # Commit the transaction
        # Cannot refresh after delete because there is no data in the database


def update_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        results = session.exec(statement)
        hero = results.first()
        print("Hero:", hero)
        hero.age = 56
        session.add(hero)
        session.commit()
        session.refresh(hero)
        print("Hero:", hero)


def select_heroes_team():
    with Session(engine) as session:
        # statement = select(Hero, Team).where(Hero.team_id == Team.id)
        statement = select(Hero, Team).join(Team)
        results = session.exec(statement)
        for hero, team in results:
            print("Hero:", hero, "Team:", team)


# Code above omitted 👆

def select_heroes_team2():
    with Session(engine) as session:
        statement = select(Hero, Team).join(Team, isouter=True)  # LEFT OUTER JOIN
        results = session.exec(statement)
        for hero, team in results:
            print("Hero:", hero, "Team:", team)


# Code below omitted 👇

# create_heroes()
# delete_hero()
# get_hero()
# get_hero_name_and_age()
# update_heroes()
# select_heroes_team()
select_heroes_team2()
