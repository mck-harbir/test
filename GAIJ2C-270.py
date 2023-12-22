using Grand.Business.Core.Interfaces.Catalog.Categories;
using Grand.Business.Core.Interfaces.Catalog.Products;
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
using Grand.Domain.Seo;
using Grand.Infrastructure;
using Grand.Web.Admin.Extensions;
using Grand.Web.Admin.Interfaces;
using Grand.Web.Admin.Models.Catalog;
using Grand.Web.Common.DataSource;
using Grand.Web.Common.Extensions;
using Grand.Web.Common.Filters;
using Grand.Web.Common.Security.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;



```csharp
/// <summary>
/// Returns a view with the social media buttons for the specified product.
/// </summary>
/// <param name="model">The product model.</param>
/// <returns>The view with the social media buttons.</returns>
public virtual IActionResult ProductSocialMediaButtons(ProductModel model)
{
    // Check if the current customer is authenticated
    if (!await _workContext.CurrentCustomer.IsAuthenticated())
    {
        return RedirectToAction("Login",