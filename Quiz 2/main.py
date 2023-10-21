from db_proxy import DataBaseManager as DBProxy
from anime_base import Anime


def main():
    database_name = "anime_database.db"
    with DBProxy(database_name) as db:
        db.connect()

        while True:
            print("\nAnime Database Menu:")
            print("1. Add Anime")
            print("2. Delete Anime")
            print("3. Mark as Seen")
            print("4. View All Anime")
            print("5. View Anime by Sport")
            print("6. Random Unseen Anime")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter the name of the anime: ")
                sport = input("Enter the sport of the anime: ")
                finished_airing = (
                    input("Is the anime finished airing? (True/False): ").lower()
                    == "true"
                )
                rating = float(input("Enter the rating (e.g., 7.5): "))
                anime = Anime(None, name, sport, finished_airing, rating)
                db.insert_row(anime)
                print("Anime added successfully!")

            elif choice == "2":
                id = input("Enter the ID of the anime to delete: ")
                db.delete_row(id)
                print("Anime deleted successfully!")

            elif choice == "3":
                id = input("Enter the ID of the anime to mark as seen: ")
                db.mark_as_seen(id)
                print("Anime marked as seen!")

            elif choice == "4":
                db.select_all()

            elif choice == "5":
                sport = input("Enter the sport to filter by: ")
                db.select_by_sport(sport)

            elif choice == "6":
                db.select_random()

            elif choice == "7":
                db.disconnect()
                print("Goodbye!")
                break


if __name__ == "__main__":
    main()
