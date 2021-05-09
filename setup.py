import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="announcement_webapp",
    version="0.0.1",

    description="A CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "announcement_webapp"},
    packages=setuptools.find_packages(where="announcement_webapp"),

    install_requires=[
        "aws-cdk.core==1.102.0",
        "aws-cdk.aws-lambda==1.102.0",
        "aws-cdk.aws-apigateway==1.102.0",
        "aws-cdk.core==1.102.0",
        "aws-cdk.aws-dynamodb==1.102.0",
        "aws-cdk.aws-lambda-python==1.102.0",
    ],

    python_requires=">=3.8",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
