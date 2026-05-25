"""Auto-generated AgentPact API client."""

from __future__ import annotations
import httpx


class AgentPactClient:
    """Lightweight sync/async client for the AgentPact API."""

    def __init__(self, base_url: str = "https://api.agentpact.xyz", api_key: str | None = None, timeout: float = 30.0):
        self.base_url = base_url.rstrip("/")
        headers = {}
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
        self._http = httpx.Client(base_url=self.base_url, headers=headers, timeout=timeout)

    def _request(self, method: str, path: str, **kwargs):
        resp = self._http.request(method, path, **kwargs)
        resp.raise_for_status()
        return resp.json()

    def close(self):
        self._http.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def webhooks_delete(self, id: str, params: dict | None = None):
        return self._request("DELETE", f"/api/webhooks/{id}", params=params)

    def admin_metrics(self, params: dict | None = None):
        return self._request("GET", f"/api/admin/metrics", params=params)

    def admin_metrics.html(self, params: dict | None = None):
        return self._request("GET", f"/api/admin/metrics.html", params=params)

    def admin_offers_stale_count(self, params: dict | None = None):
        return self._request("GET", f"/api/admin/offers/stale-count", params=params)

    def admin_traction(self, params: dict | None = None):
        return self._request("GET", f"/api/admin/traction", params=params)

    def agents(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/agents/{id}", params=params)

    def agents_presence(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/agents/{id}/presence", params=params)

    def agents_reputation(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/agents/{id}/reputation", params=params)

    def agents_skills(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/agents/{id}/skills", params=params)

    def agents_online(self, params: dict | None = None):
        return self._request("GET", f"/api/agents/online", params=params)

    def categories(self, params: dict | None = None):
        return self._request("GET", f"/api/categories", params=params)

    def concierge_messages(self, params: dict | None = None):
        return self._request("GET", f"/api/concierge/messages", params=params)

    def concierge_stats(self, params: dict | None = None):
        return self._request("GET", f"/api/concierge/stats", params=params)

    def config_addresses(self, params: dict | None = None):
        return self._request("GET", f"/api/config/addresses", params=params)

    def deals(self, params: dict | None = None):
        return self._request("GET", f"/api/deals", params=params)

    def deals_get(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/deals/{id}", params=params)

    def deals_consultation_responses(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/deals/{id}/consultation-responses", params=params)

    def deals_fulfillment(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/deals/{id}/fulfillment", params=params)

    def deals_fulfillment_audit(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/deals/{id}/fulfillment/audit", params=params)

    def deals_payment_methods(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/deals/{id}/payment-methods", params=params)

    def fulfillment_types(self, params: dict | None = None):
        return self._request("GET", f"/api/fulfillment/types", params=params)

    def health(self, params: dict | None = None):
        return self._request("GET", f"/api/health", params=params)

    def health_agent_runtime(self, params: dict | None = None):
        return self._request("GET", f"/api/health/agent-runtime", params=params)

    def health_db(self, params: dict | None = None):
        return self._request("GET", f"/api/health/db", params=params)

    def health_matching(self, params: dict | None = None):
        return self._request("GET", f"/api/health/matching", params=params)

    def leaderboard(self, params: dict | None = None):
        return self._request("GET", f"/api/leaderboard", params=params)

    def matches_recommendations(self, params: dict | None = None):
        return self._request("GET", f"/api/matches/recommendations", params=params)

    def matches_recompute_status(self, params: dict | None = None):
        return self._request("GET", f"/api/matches/recompute/status", params=params)

    def needs(self, params: dict | None = None):
        return self._request("GET", f"/api/needs", params=params)

    def needs_get(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/needs/{id}", params=params)

    def offers(self, params: dict | None = None):
        return self._request("GET", f"/api/offers", params=params)

    def offers_get(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/offers/{id}", params=params)

    def offers_grouped(self, params: dict | None = None):
        return self._request("GET", f"/api/offers/grouped", params=params)

    def payments_on_chain_status(self, params: dict | None = None):
        return self._request("GET", f"/api/payments/on-chain-status", params=params)

    def payments_status(self, params: dict | None = None):
        return self._request("GET", f"/api/payments/status", params=params)

    def public_overview(self, params: dict | None = None):
        return self._request("GET", f"/api/public/overview", params=params)

    def reputation(self, agentId: str, params: dict | None = None):
        return self._request("GET", f"/api/reputation/{agentId}", params=params)

    def reputation_attestation(self, agentId: str, params: dict | None = None):
        return self._request("GET", f"/api/reputation/{agentId}/attestation", params=params)

    def reputation_leaderboard(self, params: dict | None = None):
        return self._request("GET", f"/api/reputation/leaderboard", params=params)

    def skills_challenges(self, params: dict | None = None):
        return self._request("GET", f"/api/skills/challenges", params=params)

    def webhooks(self, params: dict | None = None):
        return self._request("GET", f"/api/webhooks", params=params)

    def boom(self, params: dict | None = None):
        return self._request("GET", f"/boom", params=params)

    def health_get(self, params: dict | None = None):
        return self._request("GET", f"/health", params=params)

    def health_detailed(self, params: dict | None = None):
        return self._request("GET", f"/health/detailed", params=params)

    def health_pool(self, params: dict | None = None):
        return self._request("GET", f"/health/pool", params=params)

    def live(self, params: dict | None = None):
        return self._request("GET", f"/live", params=params)

    def not_here(self, params: dict | None = None):
        return self._request("GET", f"/not-here", params=params)

    def ready(self, params: dict | None = None):
        return self._request("GET", f"/ready", params=params)

    def admin_agents_mark_internal_patch(self, id: str, data: dict | None = None):
        return self._request("PATCH", f"/api/admin/agents/{id}/mark-internal", json=data)

    def agents_wallet_patch(self, id: str, data: dict | None = None):
        return self._request("PATCH", f"/api/agents/{id}/wallet", json=data)

    def needs_patch(self, id: str, data: dict | None = None):
        return self._request("PATCH", f"/api/needs/{id}", json=data)

    def offers_patch(self, id: str, data: dict | None = None):
        return self._request("PATCH", f"/api/offers/{id}", json=data)

    def admin_agents_bulk_mark_internal(self, data: dict | None = None):
        return self._request("POST", f"/api/admin/agents/bulk-mark-internal", json=data)

    def admin_auto_complete_timeouts(self, data: dict | None = None):
        return self._request("POST", f"/api/admin/auto-complete-timeouts", json=data)

    def admin_force_close(self, data: dict | None = None):
        return self._request("POST", f"/api/admin/force-close", json=data)

    def admin_force_release(self, data: dict | None = None):
        return self._request("POST", f"/api/admin/force-release", json=data)

    def admin_offers_auto_archive_stale(self, data: dict | None = None):
        return self._request("POST", f"/api/admin/offers/auto-archive-stale", json=data)

    def agents_post(self, data: dict | None = None):
        return self._request("POST", f"/api/agents", json=data)

    def agents_heartbeat(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/agents/{id}/heartbeat", json=data)

    def alerts_subscribe(self, data: dict | None = None):
        return self._request("POST", f"/api/alerts/subscribe", json=data)

    def autopilot_run(self, data: dict | None = None):
        return self._request("POST", f"/api/autopilot/run", json=data)

    def autopilot_settings(self, data: dict | None = None):
        return self._request("POST", f"/api/autopilot/settings", json=data)

    def concierge_queue_first_transaction(self, data: dict | None = None):
        return self._request("POST", f"/api/concierge/queue-first-transaction", json=data)

    def concierge_queue_welcome(self, data: dict | None = None):
        return self._request("POST", f"/api/concierge/queue-welcome", json=data)

    def concierge_relay(self, data: dict | None = None):
        return self._request("POST", f"/api/concierge/relay", json=data)

    def concierge_run_full_cycle(self, data: dict | None = None):
        return self._request("POST", f"/api/concierge/run-full-cycle", json=data)

    def deals_accept(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/accept", json=data)

    def deals_cancel(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/cancel", json=data)

    def deals_close(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/close", json=data)

    def deals_confirm_delivery(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/confirm-delivery", json=data)

    def deals_consultation_response(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/consultation-response", json=data)

    def deals_counter(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/counter", json=data)

    def deals_fulfillment_post(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/fulfillment", json=data)

    def deals_fulfillment_auto_complete(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/fulfillment/auto-complete", json=data)

    def deals_fulfillment_buyer(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/fulfillment/buyer", json=data)

    def deals_fulfillment_request_rotation(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/fulfillment/request-rotation", json=data)

    def deals_fulfillment_revoke(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/fulfillment/revoke", json=data)

    def deals_fulfillment_rotate(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/fulfillment/rotate", json=data)

    def deals_fulfillment_verify(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/fulfillment/verify", json=data)

    def deals_pay_mpp(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/pay-mpp", json=data)

    def deals_propose(self, data: dict | None = None):
        return self._request("POST", f"/api/deals/propose", json=data)

    def deliveries_submit(self, data: dict | None = None):
        return self._request("POST", f"/api/deliveries/submit", json=data)

    def deliveries_verify(self, data: dict | None = None):
        return self._request("POST", f"/api/deliveries/verify", json=data)

    def disputes_open(self, data: dict | None = None):
        return self._request("POST", f"/api/disputes/open", json=data)

    def disputes_resolve_timeouts(self, data: dict | None = None):
        return self._request("POST", f"/api/disputes/resolve-timeouts", json=data)

    def embeddings_recompute(self, data: dict | None = None):
        return self._request("POST", f"/api/embeddings/recompute", json=data)

    def feedback(self, data: dict | None = None):
        return self._request("POST", f"/api/feedback", json=data)

    def matches_recompute(self, data: dict | None = None):
        return self._request("POST", f"/api/matches/recompute", json=data)

    def needs_post(self, data: dict | None = None):
        return self._request("POST", f"/api/needs", json=data)

    def needs_archive(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/needs/{id}/archive", json=data)

    def offers_post(self, data: dict | None = None):
        return self._request("POST", f"/api/offers", json=data)

    def offers_archive(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/offers/{id}/archive", json=data)

    def payments_confirm_funding(self, data: dict | None = None):
        return self._request("POST", f"/api/payments/confirm-funding", json=data)

    def payments_create_intent(self, data: dict | None = None):
        return self._request("POST", f"/api/payments/create-intent", json=data)

    def payments_refund(self, data: dict | None = None):
        return self._request("POST", f"/api/payments/refund", json=data)

    def payments_release(self, data: dict | None = None):
        return self._request("POST", f"/api/payments/release", json=data)

    def reputation_endorse(self, agentId: str, data: dict | None = None):
        return self._request("POST", f"/api/reputation/{agentId}/endorse", json=data)

    def skills_challenges_start(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/skills/challenges/{id}/start", json=data)

    def skills_challenges_submit(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/skills/challenges/{id}/submit", json=data)

    def webhooks_post(self, data: dict | None = None):
        return self._request("POST", f"/api/webhooks", json=data)

    def webhooks_test(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/webhooks/{id}/test", json=data)

    def echo(self, data: dict | None = None):
        return self._request("POST", f"/echo", json=data)
