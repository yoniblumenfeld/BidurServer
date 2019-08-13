from django.conf import settings
import pymongo

def __get_db_instance():
    return pymongo.MongoClient(settings.SCRAPERS_DB_URL)[settings.SCRAPERS_DB_NAME]

def is_collection_exists(collection_name):
    db = __get_db_instance()
    return collection_name in db.list_collection_names()

def search_db_for_keywords(keywords):
    whole_results = {}
    for keyword in keywords:
        whole_results.update({keyword:__find_results_by_keyword(keyword)})
    return whole_results

def __find_results_by_keyword(keyword):
    db = __get_db_instance()
    results_list = []
    collections_names_containing_keyword = (name for name in db.list_collection_names() if keyword in name)
    relevant_collections_list = (db.get_collection(name) for name in collections_names_containing_keyword)
    for relevant_collection in relevant_collections_list: results_list.extend(
        (doc for doc in relevant_collection.find({},{'_id':False})))
    collection = db.get_collection(settings.SCRAPERS_NO_KEYWORDS_COLLECTION_NAME)
    query = {'title': {'$regex': '.*{}.*'.format(keyword)}}
    for doc in collection.find(query,{'_id':False}): results_list.append(doc)
    return results_list
