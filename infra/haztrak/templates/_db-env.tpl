{{/*
Environment variables used to access the database
*/}}
{{- define "haztrak.db-env" }}
TRAK_DB_HOST: {{ .Values.global.db.host }}
TRAK_DB_PORT: {{ .Values.global.db.port | quote}}
TRAK_DB_NAME: {{ .Values.global.db.name }}
TRAK_DB_USER: {{ .Values.global.db.user }}
TRAK_DB_PASSWORD: {{ .Values.global.db.password }}
TRAK_DB_ENGINE: {{ .Values.global.db.engine }}
{{- end }}
