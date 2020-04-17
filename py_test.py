import json

schema = json.loads('''{
  "$id": "https://example.com/nested-schema.json",
  "title": "nested-schema",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "required": [
    "EmploymentInformation",
    "EmployeePartyID",
    "Age"
  ],
  "properties": {
    "EmployeePartyID": {
      "type": "string",
      "minLength": 1,
      "maxLength": 3
    },
    "EmploymentInformation": {
      "$ref": "#/definitions/EmploymentInformation"
    },
    "Age": {
      "type": "integer",
      "minimum": 16,
      "maximum": 80
    }
  },
  "definitions": {
    "EmploymentInformation": {
      "type": "object",
      "required": [
        "OriginalHireDate"
      ],
      "properties": {
        "OriginalHireDate": {
          "type": "string",
          "format": "date"
        },
        "Beneficiary": {
          "$ref": "#/definitions/DependantInformation"
        }
      }
    },
    "DependantInformation": {
      "type": "object",
      "required": [
        "Name"
      ],
      "properties": {
        "Name": {
          "type": "string",
          "minLength": 5
        }
      }
    }
  },
  "description": "nested-schema"
}''')

assert(get_type_for_key_path(schema, "Age") == "integer")
assert(get_type_for_key_path(schema, "EmploymentInformation.OriginalHireDate") == "string")
assert(get_type_for_key_path(schema, "EmploymentInformation.Beneficiary.Name") == "string")
assert(get_type_for_key_path(schema, "foo.bar") == None)
