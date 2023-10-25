from django.db import models


class Alumno(models.Model):
    rut_alumno = models.CharField(primary_key=True, max_length=10)
    p_nombre = models.CharField(max_length=45)
    s_nombre = models.CharField(max_length=45)
    p_apellido = models.CharField(max_length=45)
    s_apellido = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    telefono = models.IntegerField()
    carrera = models.CharField(max_length=45)
    pass_field = models.CharField(db_column='pass', max_length=45)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'alumno'


class Asignatura(models.Model):
    id_asignatura = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'asignatura'


class Asistencia(models.Model):
    id_asistencia = models.IntegerField(primary_key=True)
    fecha = models.DateField(unique=True)
    estado = models.CharField(max_length=45)
    alumno_rut_alumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='Alumno_rut_alumno')  # Field name made lowercase.
    clase_id_clase = models.ForeignKey('Clase', models.DO_NOTHING, db_column='Clase_id_clase')  # Field name made lowercase.
    latitud_alumno = models.FloatField()
    longitud_alumno = models.FloatField()

    class Meta:
        managed = False
        db_table = 'asistencia'


class Clase(models.Model):
    id_clase = models.IntegerField(primary_key=True)
    horario = models.CharField(max_length=45)
    cantidad_alumnos = models.CharField(max_length=45)
    sala_id_sala = models.ForeignKey('Sala', models.DO_NOTHING, db_column='Sala_id_sala')  # Field name made lowercase.
    seccion_id_seccion = models.ForeignKey('Seccion', models.DO_NOTHING, db_column='Seccion_id_seccion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clase'


class Profesor(models.Model):
    rut_profesor = models.CharField(primary_key=True, max_length=10)
    p_nombre = models.CharField(max_length=45)
    s_nombre = models.CharField(max_length=45)
    p_apellido = models.CharField(max_length=45)
    s_apellido = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    telefono = models.IntegerField()
    pass_field = models.CharField(db_column='pass', max_length=45)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'profesor'


class Sala(models.Model):
    id_sala = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)
    longitud = models.FloatField()
    latitud = models.FloatField()

    class Meta:
        managed = False
        db_table = 'sala'


class Seccion(models.Model):
    id_seccion = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)
    asignatura_id_asignatura = models.ForeignKey(Asignatura, models.DO_NOTHING, db_column='Asignatura_id_asignatura')  # Field name made lowercase.
    profesor_rut_profesor = models.ForeignKey(Profesor, models.DO_NOTHING, db_column='Profesor_rut_profesor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seccion'
