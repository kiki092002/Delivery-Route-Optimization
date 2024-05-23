from flask import Flask, render_template, request, jsonify
import json
import heapq

app = Flask(__name__)

with open('data/locations.json') as file:
    locations = json.load(file)


def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    seen = set()
    mins = {start: 0}
    while queue:
        (cost, v1, path) = heapq.heappop(queue)
        if v1 in seen:
            continue

        seen.add(v1)
        path = path + [v1]
        if v1 == end:
            return (cost, path)

        for v2, c in graph.get(v1, {}).items():
            if v2 in seen:
                continue
            prev = mins.get(v2, None)
            next = cost + c
            if prev is None or next < prev:
                mins[v2] = next
                heapq.heappush(queue, (next, v2, path))

    return float("inf"), []


@app.route('/')
def index():
    return render_template('index.html', locations=locations)


@app.route('/optimize', methods=['POST'])
def optimize():
    data = request.json
    start = data['start']
    end = data['end']
    cost, path = dijkstra(locations, start, end)
    return jsonify(cost=cost, path=path)


if __name__ == '__main__':
    app.run(debug=True)
