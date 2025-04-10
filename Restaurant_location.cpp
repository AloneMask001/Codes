#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() 
{
  int i, j, coordinates[10][10], num; // Declare variables for coordinates and user input
  float one, two, three, four; // Variables to store distances to restaurants

  // Initialize the 10x10 grid with all zeros
  for(i = 0; i < 10; i++)
  {
    for(j = 0; j < 10; j++)
    {
      coordinates[i][j] = 0; // Set all grid cells to 0
    }
  }

  // Mark specific coordinates as restaurant locations
  coordinates[0][0] = 1; // Restaurant 1
  coordinates[3][4] = 1; // Restaurant 2
  coordinates[5][6] = 1; // Restaurant 3
  coordinates[7][9] = 1; // Restaurant 4

  int result = 0; // Variable to store the nearest restaurant index

  // Ask the user what information they want
  do
  {
    cout << "What kind of info. you want to learn(1:nearest restaurant, 2:The gap between you and restaurants, 3:Exit): ";
    cin >> num; // Get user input
  } while (num > 3); // Repeat until a valid option is chosen

  // Ask the user for their current location
  do
  {
    cout << "What is your current location([i][j]): ";
    cin >> i >> j; // Get the user's coordinates
  } while (i < 0 || i > 10 || j < 0 || j > 10); // Ensure the location is within bounds

  // Calculate distances to each restaurant
  one = sqrt(pow(i - 0, 2) + pow(j - 0, 2)); // Distance to Restaurant 1
  two = sqrt(pow(i - 3, 2) + pow(j - 4, 2)); // Distance to Restaurant 2
  three = sqrt(pow(i - 5, 2) + pow(j - 6, 2)); // Distance to Restaurant 3
  four = sqrt(pow(i - 7, 2) + pow(j - 9, 2)); // Distance to Restaurant 4

  // Determine the nearest restaurant
  if(one == 0)
    result = 0; // User is at Restaurant 1
  else if(one < two && one < three && one < four)
    result += 1; // Restaurant 1 is the nearest
  else if(two < one && two < three && two < four)
    result += 2; // Restaurant 2 is the nearest
  else if(three < two && three < four && three < one)
    result += 3; // Restaurant 3 is the nearest
  else if(four < two && four < three && four < one)
    result += 4; // Restaurant 4 is the nearest

  // Handle the user's choice
  switch(num)
  {
    case 1: // Nearest restaurant
      if(result == 4)
        cout << "The nearest restaurant is coordinates[7][9]" << endl;
      else if (result == 3)
        cout << "The nearest restaurant is coordinates[5][6]" << endl;
      else if (result == 2)
        cout << "The nearest restaurant is coordinates[3][4]" << endl;
      else if (result == 1)
        cout << "The nearest restaurant is coordinates[0][0]" << endl;
      else if (result == 0)
        cout <<  "You're in the restaurant." << endl;
      else
        cout << "invalid" << endl;
      cout << "Exit page..." << endl;
      break;

    case 2: // Distances to all restaurants
      cout << "Nearest restaurant lists:" << endl;
      cout << fixed << setprecision(2); // Format distances to 2 decimal places
      cout << "The gap between location and restaurant (1): " << one << endl;
      cout << "The gap between location and restaurant (2): " << two << endl;
      cout << "The gap between location and restaurant (3): " << three << endl;
      cout << "The gap between location and restaurant (4): " << four << endl;
      cout << "Exit page..." << endl;
      break;

    case 3: // Exit
      cout << "Exit page..." << endl;
      break;
  }
  return 0;
}