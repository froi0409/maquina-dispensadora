class VendingMachine:
    def __init__(self):
        self.states = {"without-coin", "received-coin", "served-c1", "served-c2", "served-c3"}

        self.rules = {
            "without-coin": "request-coin",
            "received-coin": "request-code",
            "served-c1": "serve-c1-waiting",
            "served-c2": "serve-c2-waiting",
            "served-c3": "serve-c3-waiting"
        }

        self.actions = {
            "request-coin": "Inserte moneda",
            "request-code": "Ingrese código",
            "serve-c1-waiting": "Sirviendo refresco 1, espere un momento...",
            "serve-c2-waiting": "Sirviendo refresco 2, espere un momento...",
            "serve-c3-waiting": "Sirviendo refresco 3, espere un momento..."
        }

        self.model = [
            ["without-coin", "request-coin", "coin", "received-coin"],
            ["received-coin", "request-code", "c1", "served-c1"],
            ["received-coin", "request-code", "c2", "served-c2"],
            ["received-coin", "request-code", "c3", "served-c3"],
            ["served-c1", "serve-c1-waiting", "served", "without-coin"],
            ["served-c2", "serve-c2-waiting", "served", "without-coin"],
            ["served-c3", "serve-c3-waiting", "served", "without-coin"],
            ["received-coin", "request-code", "coin", "received-coin"]
        ]

        self.state = "without-coin"
        self.action = "request-coin"

    def exist_in_model(self, state, action, perception):
        for row in self.model:
            if row[0] == state and row[1] == action and row[2] == perception:
                return row[3]
        return None

    def update_state(self, state, action, perception):
        result = self.exist_in_model(state, action, perception)
        if result is not None:
            return result
        else:
            return "without-coin"
