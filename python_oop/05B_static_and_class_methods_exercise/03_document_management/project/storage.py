from typing import Collection

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category):
        self.__add_object(category, self.categories)

    def add_topic(self, topic: Topic):
        self.__add_object(topic, self.topics)

    def add_document(self, document: Document):
        self.__add_object(document, self.documents)

    def edit_category(self, category_id: int, new_name: str):
        self.__edit_object(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, *new_values):
        self.__edit_object(topic_id, self.topics, *new_values)

    def edit_document(self, document_id: int, new_name: str):
        self.__edit_object(document_id, self.documents, new_name)

    def delete_category(self, category_id: int):
        self.__delete_object(category_id, self.categories)

    def delete_topic(self, topic_id: int):
        self.__delete_object(topic_id, self.topics)

    def delete_document(self, document_id: int):
        self.__delete_object(document_id, self.documents)

    def get_document(self, document_id: int):
        return self.__find_object(document_id, self.documents)

    def __repr__(self):
        return "\n".join(str(d) for d in self.documents)

    def __edit_object(self, obj_id: int, collection: list[Category | Topic | Document], *new_values: str):
        current_obj = self.__find_object(obj_id, collection)
        if current_obj:
            current_obj.edit(*new_values)

    def __delete_object(self, obj_id: int, collection: list[Category | Topic | Document]) -> None:
        current_obj = self.__find_object(obj_id, collection)
        if current_obj:
            collection.remove(current_obj)

    @staticmethod
    def __add_object(obj: Category | Topic | Document, collection: list[Category | Topic | Document]) -> None:
        if obj not in collection:
            collection.append(obj)

    @staticmethod
    def __find_object(obj_id: int, collection: list[Category | Topic | Document]) -> Category | Topic | Document | None:
        return next((o for o in collection if o.id == obj_id), None)