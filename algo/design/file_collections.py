files = [
    {'id': 1, 'size': 100, 'collectionIds': [1]},
    {'id': 2, 'size': 300, 'collectionIds': [2, 3]},
    {'id': 3, 'size': 150, 'collectionIds': [1, 3]},
    {'id': 4, 'size': 200, 'collectionIds': [2]},
]


def get_total_file_size(collection_id):
    """
    Given a collection ID, return the total size of all files in that collection.
    """
    total_size = 0
    for file in files:
        total_size += file['size'] if file['size'] else 0
    return total_size

collection_size_map={}
def divide_file_size_by_collection(files):
    for file in files:
        collection_ids = file['collectionIds']
        size=file['size']
        share=size/len(collection_ids)

        for id in collection_ids:
            if id in collection_size_map:
                collection_size_map[id]+=share
            else:
                collection_size_map[id]=share
    return collection_size_map

divide_file_size_by_collection(files)

# https://chatgpt.com/share/6810a800-b1c0-8000-aaa1-4d1d0eed9e7f