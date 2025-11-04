from setuptools import setup

# Read long description from README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mcp-m365-mgmt",
    version="1.0.1",
    author="Thiago Beier",
    author_email="thiago.beier@gmail.com",
    description="MCP server for Microsoft 365 and Intune management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thiagogbeier/mcp-m365-mgmt",
    py_modules=["mcp_m365_mgmt", "test_client"],
    python_requires=">=3.9",
    install_requires=[
        "fastmcp>=0.1.0",
        "azure-identity>=1.25.0",
        "requests>=2.31.0",
        "python-docx>=1.1.0",
        "openpyxl>=3.1.0",
        "python-pptx>=0.6.23",
        "odfpy>=1.4.1",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "build>=0.10.0",
            "twine>=4.0.0",
            "pytest>=7.0.0",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
        "Topic :: Office/Business",
    ],
    entry_points={
        "console_scripts": [
            "m365-mgmt=mcp_m365_mgmt:main",
        ],
    },
    include_package_data=True,
)
