from _typeshed import Self
import os


class FriendShips:
    def __init__(self) -> None:
        self.baza = {}
    
    def addPerson(self, nazwa):
        if nazwa not in self.baza.keys():
            self.baza[nazwa] = []
            return 'Dodano Osobe'
        raise ValueError
    
    def addFriend(self, osoba1, osoba2):
        if osoba1 in self.baza.keys():
            self.baza[osoba1].append(osoba2)
            return 'Dodano przyjaciela'
        raise ValueError
    
    def getFriendList(self, osoba):
        if osoba in self.baza.keys():
            return self.baza[osoba]
        raise ValueError
    
    def makeFriend(self, p1, p2):
        if p1 in self.baza.keys() and p2 in self.baza.keys():
            self.addFriend(p1, p2)
            self.addFriend(p2, p1)
            return 'Dodano przyjaciół'
        raise ValueError
    
    def areFriends(self, p1, p2):
        if p2 in self.baza.keys():
            if p1 in self.getFriendList(p2):
                return True
        raise ValueError