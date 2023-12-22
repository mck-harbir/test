using Grand.Business.Core.Interfaces.Catalog.Categories;
using Grand.Business.Core.Interfaces.Catalog.Collections;
using Grand.Business.Core.Interfaces.Catalog.Products;
using Grand.Business.Core.Interfaces.Checkout.Orders;
using Grand.Business.Core.Interfaces.Common.Directory;
using Grand.Business.Core.Interfaces.Common.Localization;
using Grand.Business.Core.Interfaces.Common.Logging;
using Grand.Business.Core.Interfaces.Common.Seo;
using Grand.Business.Core.Interfaces.Customers;
using Grand.Business.Core.Interfaces.Directory;
using Grand.Business.Core.Interfaces.Localization;
using Grand.Business.Core.Interfaces.Logging;
using Grand.Business.Core.Interfaces.Seo;
using Grand.Business.Core.Utilities.Common.Security;
using Grand.Domain.Catalog;
using Grand.Domain.Common;
using Grand.Domain.Customers;
using Grand.Domain.Directory;
using Grand.Domain.Seo;
using Grand.Infrastructure;
using Grand.Web.Admin.Extensions;
using Grand.Web.Admin.Interfaces;
using Grand.Web.Admin.Models.Catalog;
using Grand.Web.Admin.Models.Common;
using Grand.Web.Admin.Models.Customers;
using Grand.Web.Admin.Models.Seo;
using Grand.Web.Common.DataSource;
using Grand.Web.Common.Extensions;
using Grand.Web.Common.Filters;
using Grand.Web.Common.Security.Authorization;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;



```csharp
/// <summary>
/// Gets the recommended products.
/// </summary>
///