import json
 import format_generation

print(format_generation())

def avro_schema():


    sample = {
        "type": "record",
        "name": "userInfo",
        "namespace": "my.example",
        "fields": [{"name": "Definition",
                    "type": {
                        "name": "Definition",
                        "type": "record",
                        "fields": [
                            {"name": "Metadata",
                             "type":"string",
                             "default" : None ,
                             "Values"  :
                             },
                            {"name": "Data Type",
                             "type": "int",
                             "default": None},
                            {"name": "Nullability",

                             },
                            "default": None},
    "type": "boolean",
    "default": None},

    ]


    {"name": "age",
     "type": "int",
     "default": -1},

    {"name": "phone",
     "type": "string",
     "default": None},

    {"name": "housenum",
     "type": "string",
     "default": None},

    {"name": "Domain Highlights",
     "type": {
         "type": "record",
         "name": "Domain Highlights",
         "fields": [
             {"name": "Total Rows",
              "type": "int",
              "default": None},

             {"name": "Cardinality",
              "type": "int",
              "default": None},

             {"name": "Cardninality %",
              "type": "float",
              "default": None},

         ]},
     "default": {}
     }
    ]
    }
    data = json.dumps(sample)
    print(data)
    return data

print(avro_schema())