# test_lote25.py
from risk_guardian import InstitutionalRiskGuardian
from execution_agent import ExecutionOMSAgent

# B17: verificar que los nuevos campos existen
rg = InstitutionalRiskGuardian(initial_capital=1730.0)
report = rg.get_status_report()
assert "pending_positions_count" in report
assert "evaluating_symbols" in report
print("✅ B17: campos presentes en RiskGuardian")
print(f"   pending_positions_count = {report['pending_positions_count']}")
print(f"   evaluating_symbols     = {report['evaluating_symbols']}")

# B15: verificar que el método existe
oms = ExecutionOMSAgent()
assert hasattr(oms, "_scan_recent_deals_for_closures")
assert hasattr(oms, "_last_deals_scan_ts")
assert hasattr(oms, "_processed_deal_tickets")
print("✅ B15: método y estado presentes en ExecutionOMS")
print(f"   _last_deals_scan_ts      = {oms._last_deals_scan_ts}")
print(f"   _processed_deal_tickets  = {oms._processed_deal_tickets}")

print("\n🎯 Ambos archivos OK.")