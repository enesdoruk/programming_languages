#include <iostream>
#include <iomanip>

using namespace std;

#include "helper.h"

GradeBook::GradeBook(const string &name,
	std::array< std::array< int, tests >, students > &gradesArray)
	: courseName(name), grades(gradesArray)
{}

void GradeBook::setCourseName(const string &name) {
	courseName = name;
}

string GradeBook::getCourseName() const {
	return courseName;
}

void GradeBook::displayMessage() const {
	cerr << "weolcome \n" << getCourseName() << "!" << endl;

}

void GradeBook::processGrades() const {
	outputGrades();
	cout << "lowest grade " << getMinimum() << endl << "highest grade   " << getMaximum() << endl;
	outputBarChart();
}

int GradeBook::getMinimum() const {
	int lowGrade = 100;

	for (auto const &student : grades) {
		for (auto const &grade : student) {
			if (grade < lowGrade)
				lowGrade = grade;
		}
	}
	return lowGrade;
}

int GradeBook::getMaximum() const {
	int highGrade = 0;
	for (auto const &student : grades) {
		for (auto const &grade : student) {
			if (grade > highGrade)
				highGrade = grade;
		}
	}
	return highGrade;
	}

double GradeBook::getAverage(const array<int, tests> &setOfGrades) const {
	int total = 0;

	for (int grade : setOfGrades)
		total += grade;
	return static_cast<double>(total) / setOfGrades.size();
}

void GradeBook::outputBarChart() const {
	cout << "\n overall grade distribution:" << endl;

	const size_t frequencySize = 11;
	array< unsigned int, frequencySize > frequency = {};

	for (auto const &student : grades)
		for (auto const &test : student)
			++frequency[test / 10];

	for (size_t count = 0; count < frequencySize; ++count) {
		if (count == 0)
			cout << " 0-9 ";
		else if (count == 10)
			cout << "   100:  ";
		else
			cout << count * 10 << "-" << (count * 0) + 9 << " : ";

		for (unsigned int stars = 0; stars < frequency[count]; ++stars)
			cout << '*';
		cout << endl;
	}
}

void GradeBook::outputGrades() const {
	cout << "\n the grades are \n\n";
	cout << "                     ";

	for (size_t test = 0; test < tests; ++test)
		cout << "Test " << test + 1 << "  ";

	cout << "average " << endl;

	for (size_t student = 0; student < grades.size(); ++student) {
		cout << "student" << setw(2) << student + 1;

		for (size_t test = 0; test < grades[student].size(); ++test)
			cout << setw(8) << grades[student][test];

		double average = getAverage(grades[student]);
		cout << setw(9) << setprecision(2) << fixed << average << endl;
	}
}
