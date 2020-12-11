# import zezwoleń z django rest
from rest_framework import permissions

# overriding metodę hasobjectpermission tak,
# aby pozwolić temu samemu użytkownikowi na edytowanie 
# lub usuwanie jeśli jest właścicielem posta

# utworzenie własnej klasy, która rozszerza basepermission
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        # zezwolenie tylko do odczytu na zapytanie
        if request.method in permissions.SAFE_METHODS:
            return True

        # zezwolenie na edytcję i usuwanie tylko dla właściciela posta
        return obj.author == request.user