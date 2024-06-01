import random

def generate_random_data():
    industries = ["Tecnología", "Finanzas", "Salud", "Gobierno", "Educación", "Energía", "Manufactura", "Retail", "Transporte", "Telecomunicaciones", "Entretenimiento", "Otra"]
    sizes = ["Microempresa", "Pequeña empresa", "Mediana empresa", "Gran empresa", "Corporación"]
    budgets = ["Muy bajo", "Bajo", "Medio", "Alto", "Muy alto"]
    maturities = ["Muy bajo", "Bajo", "Medio", "Alto", "Muy alto"]
    assets_data = ["Personales", "Financieros", "De salud", "Propiedad intelectual", "Secretos comerciales", "Otros"]
    assets_systems = ["Aplicaciones web", "Bases de datos", "Sistemas de producción", "Infraestructura de red", "Otros"]
    compliance = ["GDPR", "HIPAA", "PCI DSS", "SOX", "GLBA", "ISO 27001", "DORA", "NIS2", "Otra"]
    technologies = ["Aplicaciones web", "Bases de datos", "Aplicaciones móviles", "Infraestructura en la nube", "Sistemas de correo electrónico", "Sistemas de gestión de relaciones con los clientes (CRM)", "Sistemas de planificación de recursos empresariales (ERP)", "Sistemas de control industrial (ICS/SCADA)", "Otros"]
    policies = ["Política de seguridad de la información", "Política de control de acceso", "Política de gestión de activos", "Política de seguridad de recursos humanos", "Política de seguridad física y del entorno", "Política de gestión de las comunicaciones y operaciones", "Política de adquisición, desarrollo y mantenimiento de sistemas de información", "Política de gestión de incidentes", "Política de gestión de la continuidad del negocio", "Política de cumplimiento", "Política de auditoría interna"]

    random_data = {
        "industry": random.choice(industries),
        "size": random.choice(sizes),
        "budget": random.choice(budgets),
        "maturity": random.choice(maturities),
        "assets_data": random.choice(assets_data),
        "assets_systems": random.choice(assets_systems),
        "compliance": random.choice(compliance),
        "technologies": random.choice(technologies),
        "policies": random.choice(policies)
    }

    return random_data