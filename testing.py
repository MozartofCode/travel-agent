from travel_agent.src.travel_agent.main import create_report, create_presentation

def test_create_report():
    create_report('New York', 'Los Angeles', '2021-01-01', '2021-01-31')


def test_create_presentation():
    create_presentation('New York', 'Los Angeles', '2021-01-01', '2021-01-31')


#test_create_report()
test_create_presentation()