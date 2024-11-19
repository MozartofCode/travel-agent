from travel_agent.src.travel_agent.main import create_report, create_presentation, run_crew

def test_create_report():
    run_crew('New York', 'Los Angeles', '2025-01-01', '2025-01-31')
    create_report()


def test_create_presentation():
    run_crew('New York', 'Los Angeles', '2025-01-01', '2025-01-31')
    create_presentation()


test_create_report()
# test_create_presentation()