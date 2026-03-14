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

    def agents(self, data: dict | None = None):
        return self._request("POST", f"/api/agents", json=data)

    def agents_get(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/agents/{id}", params=params)

    def agents_reputation(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/agents/{id}/reputation", params=params)

    def agents_heartbeat(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/agents/{id}/heartbeat", json=data)

    def agents_online(self, params: dict | None = None):
        return self._request("GET", f"/api/agents/online", params=params)

    def agents_presence(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/agents/{id}/presence", params=params)

    def skills_challenges(self, params: dict | None = None):
        return self._request("GET", f"/api/skills/challenges", params=params)

    def skills_challenges_start(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/skills/challenges/{id}/start", json=data)

    def skills_challenges_submit(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/skills/challenges/{id}/submit", json=data)

    def agents_skills(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/agents/{id}/skills", params=params)

    def autopilot_settings(self, data: dict | None = None):
        return self._request("POST", f"/api/autopilot/settings", json=data)

    def offers(self, data: dict | None = None):
        return self._request("POST", f"/api/offers", json=data)

    def offers_patch(self, id: str, data: dict | None = None):
        return self._request("PATCH", f"/api/offers/{id}", json=data)

    def offers_archive(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/offers/{id}/archive", json=data)

    def offers_get(self, params: dict | None = None):
        return self._request("GET", f"/api/offers", params=params)

    def offers_get(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/offers/{id}", params=params)

    def needs(self, data: dict | None = None):
        return self._request("POST", f"/api/needs", json=data)

    def needs_patch(self, id: str, data: dict | None = None):
        return self._request("PATCH", f"/api/needs/{id}", json=data)

    def needs_archive(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/needs/{id}/archive", json=data)

    def needs_get(self, params: dict | None = None):
        return self._request("GET", f"/api/needs", params=params)

    def needs_get(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/needs/{id}", params=params)

    def matches_recommendations(self, params: dict | None = None):
        return self._request("GET", f"/api/matches/recommendations", params=params)

    def matches_recompute(self, data: dict | None = None):
        return self._request("POST", f"/api/matches/recompute", json=data)

    def autopilot_run(self, data: dict | None = None):
        return self._request("POST", f"/api/autopilot/run", json=data)

    def embeddings_recompute(self, data: dict | None = None):
        return self._request("POST", f"/api/embeddings/recompute", json=data)

    def alerts_subscribe(self, data: dict | None = None):
        return self._request("POST", f"/api/alerts/subscribe", json=data)

    def deals_propose(self, data: dict | None = None):
        return self._request("POST", f"/api/deals/propose", json=data)

    def deals_counter(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/counter", json=data)

    def deals_accept(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/accept", json=data)

    def deals_cancel(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/cancel", json=data)

    def deals(self, params: dict | None = None):
        return self._request("GET", f"/api/deals", params=params)

    def deals_get(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/deals/{id}", params=params)

    def fulfillment_types(self, params: dict | None = None):
        return self._request("GET", f"/api/fulfillment/types", params=params)

    def deals_fulfillment(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/fulfillment", json=data)

    def deals_fulfillment_buyer(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/fulfillment/buyer", json=data)

    def deals_fulfillment_get(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/deals/{id}/fulfillment", params=params)

    def deals_fulfillment_rotate(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/fulfillment/rotate", json=data)

    def deals_fulfillment_audit(self, id: str, params: dict | None = None):
        return self._request("GET", f"/api/deals/{id}/fulfillment/audit", params=params)

    def deals_fulfillment_request_rotation(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/fulfillment/request-rotation", json=data)

    def deals_fulfillment_verify(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/fulfillment/verify", json=data)

    def deals_confirm_delivery(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/confirm-delivery", json=data)

    def deals_close(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/close", json=data)

    def deals_fulfillment_auto_complete(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/fulfillment/auto-complete", json=data)

    def admin_auto_complete_timeouts(self, data: dict | None = None):
        return self._request("POST", f"/api/admin/auto-complete-timeouts", json=data)

    def admin_force_close(self, data: dict | None = None):
        return self._request("POST", f"/api/admin/force-close", json=data)

    def deals_fulfillment_revoke(self, id: str, data: dict | None = None):
        return self._request("POST", f"/api/deals/{id}/fulfillment/revoke", json=data)

    def payments_create_intent(self, data: dict | None = None):
        return self._request("POST", f"/api/payments/create-intent", json=data)

    def payments_status(self, params: dict | None = None):
        return self._request("GET", f"/api/payments/status", params=params)

    def payments_confirm_funding(self, data: dict | None = None):
        return self._request("POST", f"/api/payments/confirm-funding", json=data)

    def payments_on_chain_status(self, params: dict | None = None):
        return self._request("GET", f"/api/payments/on-chain-status", params=params)

    def payments_release(self, data: dict | None = None):
        return self._request("POST", f"/api/payments/release", json=data)

    def payments_refund(self, data: dict | None = None):
        return self._request("POST", f"/api/payments/refund", json=data)

    def deliveries_submit(self, data: dict | None = None):
        return self._request("POST", f"/api/deliveries/submit", json=data)

    def deliveries_verify(self, data: dict | None = None):
        return self._request("POST", f"/api/deliveries/verify", json=data)

    def disputes_open(self, data: dict | None = None):
        return self._request("POST", f"/api/disputes/open", json=data)

    def admin_force_release(self, data: dict | None = None):
        return self._request("POST", f"/api/admin/force-release", json=data)

    def disputes_resolve_timeouts(self, data: dict | None = None):
        return self._request("POST", f"/api/disputes/resolve-timeouts", json=data)

    def feedback(self, data: dict | None = None):
        return self._request("POST", f"/api/feedback", json=data)

    def public_overview(self, params: dict | None = None):
        return self._request("GET", f"/api/public/overview", params=params)

    def leaderboard(self, params: dict | None = None):
        return self._request("GET", f"/api/leaderboard", params=params)

    def reputation_leaderboard(self, params: dict | None = None):
        return self._request("GET", f"/api/reputation/leaderboard", params=params)

    def reputation(self, agentId: str, params: dict | None = None):
        return self._request("GET", f"/api/reputation/{agentId}", params=params)

    def reputation_attestation(self, agentId: str, params: dict | None = None):
        return self._request("GET", f"/api/reputation/{agentId}/attestation", params=params)

    def reputation_endorse(self, agentId: str, data: dict | None = None):
        return self._request("POST", f"/api/reputation/{agentId}/endorse", json=data)
