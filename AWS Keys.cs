using System;

class Program
{
    // Example AWS Access Key and Secret Key
    private const string AWS_ACCESS_KEY = "AKIAExampleAWSAccessKey1234";
    private const string AWS_SECRET_KEY = "ExampleAWSSecretKey1234567890ExampleAWSSecretKey";

    static void Main()
    {
        // Your AWS logic here
        Console.WriteLine("Using AWS Access Key: " + AWS_ACCESS_KEY);
        Console.WriteLine("Using AWS Secret Key: " + AWS_SECRET_KEY);
    }
}
