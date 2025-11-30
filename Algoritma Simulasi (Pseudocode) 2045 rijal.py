Initialize base_2024 from fiscal_data (BPS 2019–2024)
Define scenarios = {fiscal_constrained, balanced_reform, transformational_with_fiscal}

For each scenario:
    Set current_data = base_2024.copy()
    For year = 0 to years-1:
        growth_multiplier = scenario.gdp_growth / 100
        education_multiplier = scenario.education_budget_growth / 100
        tax_reform_impact = scenario.tax_reform_impact / 100

        # Update development metrics
        current_data['gdp_per_capita_usd'] *= (1 + growth_multiplier)
        current_data['hdi'] += 0.005 * (1 + education_multiplier)
        current_data['economic_structure'] = min(95, current_data['economic_structure'] + 0.3)
        current_data['investment_rate'] = min(45, current_data['investment_rate'] * (1 + investment_multiplier/10))
        current_data['education_budget'] = min(6.0, current_data['education_budget'] * (1 + education_multiplier/10))
        current_data['technology_adoption'] += 2.5 * (1 + growth_multiplier)
        current_data['infrastructure_quality'] += 2.0 * (1 + investment_multiplier)

        # Update fiscal metrics
        current_data['rasio_pajak_pdb'] = min(15, current_data['rasio_pajak_pdb'] + tax_reform_impact)
        current_data['rasio_pengeluaran_pdb'] *= (1 + 0.8 * growth_multiplier)
        current_data['net_lending_borrowing'] = min(scenario['deficit_target'], current_data['net_lending_borrowing'] + 10 * tax_reform_impact)

        # Compute development score & status
        dev_score = calculate_development_metrics(...)
        developed_status = (GDPpc >= 13000) and (HDI >= 0.8) and (ES >= 60) and (NLB >= -100)

        Append yearly results
        If developed_status and year < 2045: break
