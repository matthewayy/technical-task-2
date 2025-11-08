##Info
- Na REST API automation som sa rozhodol pouzit python resp. Pytest
- Testy su ulozene vo foldri /tests
##Obsah
- Test Case 1 – GET - List Users
    - posle request, skontroluje vsetky datove typy, porovna 'total' s poctom 'received users'
- Test Case 2 – POST – Create
    - Musel som pouzit MockAPI, kedze na povodom '/users' koncilo s 'Missing API key'
    - Data driven z ext. JSON suboru, skontroluje HTTP code, skontroluje 'ID' a 'createdAt', potvrdi response time < 100ms

##Poziadavky
- Python 3.x
- pytest
- requests

##Install
- git clone https://github.com/matthewayy/technical-task-2
- cd techtask2
- pytest .\\tests\get_users.py
- pytest .\\tests\post_users.py

##Run locally
- pip install pytest
- pip install requests