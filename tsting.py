{
    "name": "Report",
    "type": "record",
    "fields": [
        {
            "name": "Column",
            "type": "string"
        },
        {
            "name": "domain_highlights",
            "type": {
                "name": "domain_highlights",
                "type": "record",
                "fields": [
                    {
                        "name": "TotalRows",
                        "type": "int"
                    },
                    {
                        "name": "Cardinality",
                        "type": "int"
                    },
                    {
                        "name": "per_of_Cardinality",
                        "type": "int"
                    },
                    {
                        "name": "Nulls",
                        "type": "int"
                    },
                    {
                        "name": "no_of_general_formats",
                        "type": "int"
                    },
                    {
                        "name": "general_formats",
                        "type": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    }
                ]
            }
        },
        {
            "name": "MetaData",
            "type": {
                "name": "MetaData",
                "type": "record",
                "fields": [
                    {
                        "name": "Inferred",
                        "type": {
                            "name": "Inferred",
                            "type": "record",
                            "fields": [
                                {
                                    "name": "Data_type",
                                    "type": "string"
                                },
                                {
                                    "name": "data_lenght",
                                    "type": "int"
                                },
                                {
                                    "name": "Precision",
                                    "type": "int"
                                },
                                {
                                    "name": "scale",
                                    "type": "int"
                                },
                                {
                                    "name": "data_scale",
                                    "type": "int"
                                }
                            ]
                        }
                    },
                    {
                        "name": "Defined",
                        "type": {
                            "name": "Defined",
                            "type": "record"
                        }
                    }
                ]
            }
        },
        {
            "name": "inferred_data_class",
            "type": "string"
        }
    ]
}