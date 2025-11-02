from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from config.database import Base
from datetime import datetime

class Personal(Base) :

       __tablename__ ='personal'

       id = Column(Integer, primary_key=True, autoincrement=True, index=True)
       nombre = Column(String, nullable=False)
       correo = Column(String, nullable=False)
       password = Column(String, nullable=False)
       sector =  Column(String, nullable=True)
       rol = Column(String, nullable=True)   
    
       
from sqlalchemy import Column, Integer, String, ForeignKey
from config.database import Base

class Tickets(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, index=True)  # ID sigue como Integer
    sector = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    fecha_creacion = Column(String, nullable=True)      # Fecha como texto
    fecha_resolucion = Column(String, nullable=True)
    prioridad = Column(String, nullable=True)
    asignado_a = Column(String, ForeignKey('personal.id'), nullable=True)  # FK como texto
    cliente = Column(String, nullable=True)
    tipo = Column(String, nullable=True)
       