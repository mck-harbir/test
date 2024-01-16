Generate Code for this requirement: Note: The "Read Comprehensive Description" action should be available to users. The "Create Comment" action should be available only to authenticated users.

Code:

using System;
using System.Threading.Tasks;
using Grpc.Core;
using Microsoft.EntityFrameworkCore;
using Server.Data;

namespace Server.Features.Movies
{
    public class GetDetailsService : IGetDetailsService
    {
        private readonly IReadDbContext _db;

        public GetDetailsService(IReadDbContext db)
        {
            _db = db;
        }

        public async Task<GetDetailsResponse> GetDetails(GetDetailsRequest request, ServerCallContext context)
        {
            var id = request.Id;
            var item = await _db.Set<Movie>().FirstOrDefaultAsync(m => m.Id == id);

            // Handle scenario where movie not found
            if (item is null)
            {
                return null;
            }

            // Get reviews for item
            var reviews = await _db.Set<Review>()
               .Where(r => r.Movie == item)
               .Include(r => r.Author) // Pre-load author of each review
               .ToListAsync();

            // Return details response
            var response = new GetDetailsResponse
            {
                Movie = ItemToDto(item),
                Reviews = reviews.Select(review => ReviewToDto(review)).ToList()
            };
            return response;
        }

        private MovieDto ItemToDto(Movie item)
        {
            return new MovieDto
            {