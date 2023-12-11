from enum import Enum


class Message(Enum):
    SUCCESS_DATA = "API in development"
    INTERNAL_ERROR = "Erro Interno"
    MSG_API_ERROR = "Erro interno da API"
    MSG_API_ERROR_EXTER = "Erro da API externa"
    MSG_API_ERROR_BODY_INVALID = "Body da request inválido"
    DATA_ERROR = "Data Error"
    DEVELOPER = "Em desenvolvimento"
    MISSING_VERSION = "versão do banco não encontrada"
    INVALID_TOKEN = "Token inválido ou expirado"
    TYPE_ARCHIVE_INVALID = "Tipo do arquivo inválido"
    MISSING_TOKEN = "Token não encontrado"
    FORBIDDEN = "Sem permissão de acesso"
