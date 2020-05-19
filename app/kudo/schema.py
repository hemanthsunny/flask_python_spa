from marshmallow import Schema, fields

class RepoSchema(schema):
    id = fields.Int(requried=True)
    repoName = fields.Str()
    fullName = fields.Str()
    description = fields.Str()
    repoUrl = fields.URL()
    language = fields.Str()

class KudoSchema(RepoSchema):
    userId = fields.Email(required=True)
