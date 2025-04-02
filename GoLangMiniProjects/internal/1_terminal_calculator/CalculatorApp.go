package calculator

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func CalcCore() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Println("Welcome to terminal Calculator")

	fmt.Print("Enter first number: ")
	var num1Str string
	//fmt.Scanln(&num1) 	Alternative way to scan input
	num, _ := reader.ReadString('\n')
	num1Str = strings.TrimSpace(num)

	fmt.Print("Enter Operator: ")
	var oper string
	//fmt.Scanln(&oper)
	num, _ = reader.ReadString('\n')
	oper = strings.TrimSpace(num)

	fmt.Print("Enter Second number: ")
	var num2Str string
	//fmt.Scanln(&num2)
	num, _ = reader.ReadString('\n')
	num2Str = strings.TrimSpace(num)

	fmt.Println("Operation to be performed:", num1Str, oper, num2Str)
	// Following also works:
	//fmt.Println("Operation to be performed: " + num1 + " " + oper + " " + num2)

	//Converting String to Float
	num1, err1 := strconv.ParseFloat(num1Str, 64)
	num2, err2 := strconv.ParseFloat(num2Str, 64)

	if err1 != nil || err2 != nil {
		fmt.Println("Error: Invalid input numbers. Please enter numerals")
	}

	result, error := calculate(&num1, &num2, &oper)
	if error != nil {
		fmt.Print(error)
	} else {
		fmt.Printf("Result: %.2f\n", *result)
	}

}

func calculate(num1, num2 *float64, oper *string) (*float64, error) {
	result := 0.0

	switch *oper {
	case "+":
		result = *num1 + *num2
	case "-":
		result = *num1 - *num2
	case "*":
		result = *num1 * *num2
	case "/":
		if *num2 == 0 {
			return nil, fmt.Errorf("Error: Division by 0")
		}
		result = *num1 / *num2
	default:
		return nil, fmt.Errorf("Error: Unsupported Operator: %s", *oper)
	}

	return &result, nil
}

/*
calcCore() (lowercase) - Not exported, cannot be called from other packages
CalcCore() (capital C) - Exported, can be called from other packages

The benefit of doing it this way over using keywords to define exportedness (`extern`, `public`, etc.) is that making it a part of the name ensures that
    anywhere an identifier is used you can tell if it is exported or not without having to find where it was defined (to see if the definition contains a keyword).
*/

/*
When to Use Pointers

Returning a pointer (*float64) is generally unnecessary for simple types like float64, int, or string. Pointers are more useful when:

    You want to avoid copying large structs.
    You need to modify the original value in the calling function.

*/
