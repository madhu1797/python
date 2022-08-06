from parent_class import MembersDB
import pytest

def test_Senpai_db():
    db=MembersDB()
    db.Save_DB_Values('data.json')
    Senpai_data = db.get_data()
    print(senpai_data)
    assert Senpai_data.Name == "Senpai"


test_Senpai_db()
