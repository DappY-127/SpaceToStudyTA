SCHEMA_FOR_ALL_USERS = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "mainSubjects": {
                        "type": "object",
                        "required": ["student", "tutor"],
                        "properties": {
                            "student": {
                                "type": "array",
                                "items": {
                                    "type": ["object", "string"],
                                    "required": ["_id", "name", "category", "totalOffers"],
                                    "properties": {
                                        "_id": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        },
                                        "category": {
                                            "type": "string"
                                        },
                                        "totalOffers": {
                                            "type": "number"
                                        }
                                    }
                                }
                            },
                            "tutor": {
                                "type": "array",
                                "items": {
                                    "type": ["object", "string"],
                                    "required": ["_id", "name", "category", "totalOffers"],
                                    "properties": {
                                        "_id": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        },
                                        "category": {
                                            "type": "string"
                                        },
                                        "totalOffers": {
                                            "type": "number"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "totalReviews": {
                        "type": "object",
                        "required": ["student", "tutor"],
                        "properties": {
                            "student": {
                                "type": "number"
                            },
                            "tutor": {
                                "type": "number"
                            }
                        }
                    },
                    "averageRating": {
                        "type": "object",
                        "required": ["student", "tutor"],
                        "properties": {
                            "student": {
                                "type": "number"
                            },
                            "tutor": {
                                "type": "number"
                            }
                        }
                    },
                    "status": {
                        "type": "object",
                        "required": ["student", "tutor", "admin"],
                        "properties": {
                            "student": {
                                "type": "string",
                                "enum": ["active", "blocked"]
                            },
                            "tutor": {
                                "type": "string",
                                "enum": ["active", "blocked"]
                            },
                            "admin": {
                                "type": "string",
                                "enum": ["active", "blocked"]
                            }
                        }
                    },
                    "_id": {
                        "type": "string"
                    },
                    "role": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["student", "tutor"]
                        }
                    },
                    "firstName": {
                        "type": "string"
                    },
                    "lastName": {
                        "type": "string"
                    },
                    "email": {
                        "type": "string"
                    },
                    "lastLogin": {
                        "type": ["string", "null"],
                        "format": "date-time"
                    },
                    "FAQ": {
                        "type": "object",
                        "required": ["student", "tutor"],
                        "properties": {
                            "student": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "required": ["question", "_id", "answer"],
                                    "properties": {
                                        "question": {
                                            "type": "string"
                                        },
                                        "_id": {
                                            "type": "string"
                                        },
                                        "answer": {
                                            "type": "string"
                                        }
                                    }
                                }
                            },
                            "tutor": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "required": ["question", "_id", "answer"],
                                    "properties": {
                                        "question": {
                                            "type": "string"
                                        },
                                        "_id": {
                                            "type": "string"
                                        },
                                        "answer": {
                                            "type": "string"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "createdAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "updatedAt": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "nativeLanguage": {
                        "type": "string"
                    },
                    "address": {
                        "type": "object",
                        "required": ["country", "city"],
                        "properties": {
                            "country": {
                                "type": "string"
                            },
                            "city": {
                                "type": "string"
                            }
                        }
                    },
                    "professionalSummary": {
                        "type": "string"
                    },
                    "photo": {
                        "type": "string"
                    },
                    "categories": {
                        "type": "array",
                        "items": {
                            "$ref": "categories/schemas.py#/SCHEMA_FOR_ALL_CATEGORIES"
                        }
                    }
                },
                "required": [
                    "mainSubjects",
                    "totalReviews",
                    "averageRating",
                    "status",
                    "_id",
                    "role",
                    "firstName",
                    "lastName",
                    "email",
                    "createdAt",
                    "updatedAt"
                ]
            }
        },
        "count": {
            "type": "number"
        }
    },
    "required": ["items", "count"],
}
