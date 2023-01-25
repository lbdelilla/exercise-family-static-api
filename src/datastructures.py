
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [            {
                "id": 1,
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "Lucky Numbers": [7, 13, 22]
            },
            {
                "id": 2,
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "Lucky Numbers": [10, 14, 3]
            },
            {
                "id": 3,
                "first_name": "Jimmy",
                "last_name":  self.last_name,
                "age": 5,
                "Lucky Numbers": [1]
            }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        ## you have to implement this method
        ## append the member to the list of _members
        # member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        ## you have to implement this method
        ## loop the list and delete the member with the given id
         for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True

    # def update_member(self, id, member):
    #     ## you have to implement this method
    #     ## loop the list and replace the member with the given id
    #     pass


    def get_member(self, id):
        ## you have to implement this method
        ## loop all the members and return the one with the given id
        for member in self._members:
            if member["id"] == id:
                return member
     

    def get_all_members(self):  
        return self._members


     