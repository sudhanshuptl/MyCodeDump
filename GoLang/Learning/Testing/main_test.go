package main

import ("testing")

func TestCalculate(t *testing.T){
	if(Calculation(2) != 4){
		t.Error("Expected 2 + 2 is 4")
	}
}

func TestTableCalculate(t *testing.T){
	var tests = []struct{
		input int
		expected int
	}{

		{2,4},
		{-1, 1},
		{0,2},
		{999, 1001},
	}

	for _,test := range tests{
		if output := Calculation(test.input); output !=  test.expected{
			t.Error("Test failed {} inputted , {} expected, recieved : {}", test.input, test.expected, output)
		}
	}
}

// RUn test : go test