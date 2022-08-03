import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="infrastructure_python_cdk",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "infrastructure_python_cdk"},
    packages=setuptools.find_packages(where="infrastructure_python_cdk"),

    install_requires=[
        "aws-cdk.core==1.167.0", "aws_cdk.aws_ec2", "aws_cdk.aws_autoscaling", "aws_cdk.aws_elasticloadbalancingv2"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
