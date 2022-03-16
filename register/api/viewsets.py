from rest_framework import viewsets

from register.models import Register
from register.api.serializers import RegisterSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    """
    Create new record
    curl -X POST -H "Content-Type: application/json" -d '{"name": "Lucas", "email": "lucas@gmail.com", "department": "R"}' http://127.0.0.1:8000/api/create/

    List all records
    curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/list/

    Filter one record
    curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/list/1/

    Update all fields
    curl -X PUT -H "Content-Type: application/json" -d '{"name": "Marcos", "email": "marcos@gmail.com", "department": "R"}' http://127.0.0.1:8000/api/update/1/

    Update one field only
    curl -X PUT -H "Content-Type: application/json" -d '{"name": "Roger"}' http://127.0.0.1:8000/api/update/1/

    Delete one record
    curl -X DELETE http://127.0.0.1:8000/api/delete/1/
    """
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
