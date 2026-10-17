class List:
    def iterateJSON(self, data = []):
        users = [d['name'] for d in data if bool(d['is_active']) == True]
        return users

if __name__ == "__main__":
    list = List()
    users_database = [
        {"id": 101, "name": "Alice", "role": "admin", "is_active": 1},
        {"id": 102, "name": "Bob", "role": "user", "is_active": 1},
        {"id": 103, "name": "Charlie", "role": "editor", "is_active": 0}
    ]

    active_users = list.iterateJSON(users_database)

    print("active users =>", active_users)
