class UserProfile:


    def __init__(self, id: int, code: str, name: str, avatar: str, email: str, socket_connection_token: str, **kwargs):
        """
        Obtains user profile information. Requires user authorization with the oauth-user-show scope

        :param id: The unique and unchangeable user identifier;
        :param code: The unique user name;
        :param name: The unique displayed user name;
        :param avatar: The URL to the personalized graphical illustration;
        :param email: The email address;
        :param socket_connection_token: Centrifugo connection token;

        """
        self.id = id
        self.code = code
        self.name = name
        self.avatar = avatar
        self.email = email
        self.socket_connection_token = socket_connection_token

    def __repr__(self):
        return str(self.__dict__)
