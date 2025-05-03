from app import app, db
from models import Question

def create_questions():
    with app.app_context():
        db.create_all()

        questions = [
            Question(
                text="Quelle est la capitale du Sénégal ?",
                option1="Dakar",
                option2="Thiès",
                option3="Saint-Louis",
                option4="Kaolack",
                correct=1,
                difficulty=0.5,
                time_limit=30
            ),
            Question(
                text="Quel est le plat national sénégalais ?",
                option1="Thiéboudienne",
                option2="Yassa",
                option3="Mafé",
                option4="Accara",
                correct=1,
                difficulty=1.0,
                time_limit=45
            ),
            Question(
                text="En quelle année le Sénégal a-t-il obtenu son indépendance ?",
                option1="1958",
                option2="1960",
                option3="1962",
                option4="1975",
                correct=2,
                difficulty=1.2,
                time_limit=40
            ),
            Question(
                text="Quel fleuve traverse le Sénégal ?",
                option1="Le Niger",
                option2="Le Congo",
                option3="Le Sénégal",
                option4="Le Nil",
                correct=3,
                difficulty=1.5,
                time_limit=50
            ),
            Question(
                text="Quelle est la monnaie du Sénégal ?",
                option1="Franc CFA",
                option2="Dinar",
                option3="Eco",
                option4="Dirham",
                correct=1,
                difficulty=0.8,
                time_limit=35
            ),
            Question(
                text="Qui fut le premier président du Sénégal ?",
                option1="Abdou Diouf",
                option2="Léopold Sédar Senghor",
                option3="Abdoulaye Wade",
                option4="Macky Sall",
                correct=2,
                difficulty=1.8,
                time_limit=60
            ),
            Question(
                text="Quelle île historique est classée au patrimoine mondial de l'UNESCO ?",
                option1="Île de Gorée",
                option2="Île de Ngor",
                option3="Îles Saloum",
                option4="Île de Karabane",
                correct=1,
                difficulty=1.3,
                time_limit=45
            ),
            Question(
                text="Comment s'appelle le stade national du Sénégal ?",
                option1="Stade Léopold Senghor",
                option2="Stade Demba Diop",
                option3="Stade Abdoulaye Wade",
                option4="Stade de l'Amitié",
                correct=1,
                difficulty=1.6,
                time_limit=50
            ),
            Question(
                text="Quel événement sportif international était organisé au Sénégal ?",
                option1="Coupe du Monde de Football",
                option2="Jeux Olympiques",
                option3="Rallye Dakar",
                option4="Tour de France",
                correct=3,
                difficulty=1.4,
                time_limit=45
            ),
            Question(
                text="Quelle langue officielle est utilisée au Sénégal ?",
                option1="Anglais",
                option2="Portugais",
                option3="Français",
                option4="Arabe",
                correct=3,
                difficulty=0.7,
                time_limit=30
            )
        ]

        db.session.bulk_save_objects(questions)
        db.session.commit()
        print("10 questions sur le Sénégal ajoutées à la base de données !")

if __name__ == "__main__":
    create_questions()