from gql import gql


class CustomerCreateInput:
    def __init__(self, business_id, name, contact_first_name,
                 contact_last_name, contact_email, city, postal_code,
                 province_code, country_code, currency):
        self.businessId = business_id
        self.name = name
        self.firstName = contact_first_name
        self.lastName = contact_last_name
        self.email = contact_email

        self.city = city
        self.postalCode = postal_code
        self.provinceCode = province_code
        self.countryCode = country_code

        self.currency = currency

    @property
    def address(self):
        return {
            "city": self.city,
            "postalCode": self.postalCode,
            "provinceCode": self.provinceCode,
            "countryCode": self.countryCode
        }

    def as_variable(self):
        return {
            "input": {
                "businessId": f"{self.businessId}",
                "name": f"{self.name}",
                "firstName": f"{self.firstName}",
                "lastName": f"{self.lastName}",
                "email": f"{self.email}",
                "address": self.address,
                "currency": self.currency
            }
        }


class Mutation:
    def __init__(self, wave_connection):
        """
        The Mutation object should only be initialized from the WaveApps.__init__(...) method.
        :param wave_connection: WaveApps object
        """
        self.wave = wave_connection

    def create_customer(self, input: CustomerCreateInput):

        mutation = gql(f"""
        mutation ($input: CustomerCreateInput!) {{
          customerCreate(input: $input) {{
            didSucceed
            inputErrors {{
              code
              message
              path
            }}
            customer {{
              id
              name
              firstName
              lastName
              email
              address {{
                addressLine1
                addressLine2
                city
                province {{
                  code
                  name
                }}
                country {{
                  code
                  name
                }}
                postalCode
              }}
              currency {{
                code
              }}
            }}
          }}
        }}
        """)
        self.wave.client.execute(mutation, variable_values=input.as_variable())
