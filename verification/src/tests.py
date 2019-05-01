

TESTS = {
    "Basics": [
        {
            "input": [{
                'CAC': 10.0,
                'ATX': 390.2,
                'WIG': 1.2
            }],
            "answer": 'ATX'
        },
        {
            "input": [{
                'CAC': 91.1,
                'ATX': 1.01,
                'TASI': 120.9
            }],
            "answer": 'TASI'
        }
    ],
    "Extra": [
        {
            "input": [{
                'ATX': 230.0,
                'GOOG': 100000.01
            }],
            "answer": 'GOOG'
        }
    ]
}
