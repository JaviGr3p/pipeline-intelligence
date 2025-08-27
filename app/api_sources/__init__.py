from app.extractor.hibp import fetch_hibp_breaches
from app.extractor.shadowserver import fetch_shadowserver_reports
from app.extractor.rss_feeds import fetch_rss_news
from app.extractor.alienvault import fetch_alienvault_pulses
from app.extractor.intelx import fetch_intelx_data


def fetch_all_sources():
    incidents = []

    try:
        print("🔍 Fetching HIBP breaches...")
        hibp_data = fetch_hibp_breaches()
        incidents.extend(hibp_data)
    except Exception as e:
        print(f"❌ Error fetching HIBP: {e}")

    try:
        print("🔍 Fetching Shadowserver reports...")
        shadow_data = fetch_shadowserver_reports()
        incidents.extend(shadow_data)
    except Exception as e:
        print(f"❌ Error fetching Shadowserver: {e}")

    try:
        print("🔍 Actualizando RSS news feeds...")
        rss_data = fetch_rss_news()
        incidents.extend(rss_data)
    except Exception as e:
        print(f"❌ Error al obtener información RSS feeds: {e}")

    try:
        print("🔍 Obteniendo datos de AlienVault...")
        otx_data = fetch_alienvault_pulses()
        incidents.extend(otx_data)
    except Exception as e:
        print(f"❌ Error sin información AlienVault: {e}")

    try:
        print("🔍 Encontrando información IntelX...")

        # Agrega aquí tus términos de búsqueda
        search_terms = ["ataque", "ransomware", "cve"]

        for term in search_terms:
            try:
                intelx_data = fetch_intelx_data(term)
                incidents.extend(intelx_data)
            except Exception as single_error:
                print(f"❌ Error al buscar '{term}' en IntelX: {single_error}")

    except Exception as e:
        print(f"❌ Error sin información IntelX: {e}")

    return incidents


__all__ = ['fetch_all_sources']
